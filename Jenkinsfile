// updated to use python:3.10 docker image
pipeline {
  agent {
    docker { image 'python:3.10' }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh '''
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }
    stage('Run tests') {
      steps {
        sh 'pytest -q'
      }
    }
    stage('Security Scan') {
      steps {
        sh '''
          pip install bandit safety
          echo "=== Running Bandit (code security) ==="
          bandit -r . || true
          echo "=== Running Safety (dependency check) ==="
          safety check -r requirements.txt || true
        '''
      }
    }
  }
}
