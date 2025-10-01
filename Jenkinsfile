pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Ambil kode dari repo
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Hello from Jenkins!"'
            }
        }
    }
}
