pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hannisadafitriaa-boop/ci-cd-comparison.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv curl
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -q
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install bandit safety
                    echo "=== Running Bandit (code security) ==="
                    bandit -r . || true
                    echo "=== Running Safety (dependency check) ==="
                    safety check -r requirements.txt || true
                '''
            }
        }

        stage('Deploy to Heroku') {
            steps {
                withCredentials([string(credentialsId: 'HEROKU_API_KEY', variable: 'HEROKU_API_KEY')]) {
                    sh '''
                        echo "=== Deploying to Heroku ==="
                        curl https://cli-assets.heroku.com/install.sh | sh
                        heroku login -i <<EOF
${HEROKU_EMAIL}
${HEROKU_API_KEY}
EOF
                        heroku git:remote -a nama-aplikasi-kamu
                        git push heroku main
                    '''
                }
            }
        }
    }
}
