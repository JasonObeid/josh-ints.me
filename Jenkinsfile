pipeline {
  agent any
  stages {
    stage('Pre-build') {
      steps {
        sh 'sudo git clean -fdx'
      }
    }

    stage('Build') {
      steps {
        dir(path: 'src') {
          sh '''npm install
npm run build'''
        }

      }
    }

    stage('Deploy') {
      steps {
        sh '''sudo systemctl restart nginx
sudo systemctl restart josh'''
      }
    }

  }
}