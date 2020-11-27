pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'sudo git clean -fdx'
        dir(path: 'src') {
          sh '''npm install
          npm run build'''
        }

      }
    }

    stage('Test') {
      steps {
        echo 'test here'
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