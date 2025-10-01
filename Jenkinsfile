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
          apt-get install -y python3 python3-pip python3-venv
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
          pip install pytest pip-audit bandit
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
    stage('Security Scan - Dependencies') {
      steps {
        sh '''
          . venv/bin/activate
          echo "=== Running pip-audit ==="
          pip-audit -r requirements.txt || true
        '''
      }
    }
    stage('Security Scan - Code') {
      steps {
        sh '''
          . venv/bin/activate
          echo "=== Running bandit ==="
          bandit -r . || true
        '''
      }
    }
  }
}
