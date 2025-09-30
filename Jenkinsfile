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
          apt-get install -y python3 python3-pip
          python3 --version
          pip3 --version
        '''
      }
    }
    stage('Install dependencies') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Run tests') {
      steps {
        sh 'pytest -q'
      }
    }
  }
}
