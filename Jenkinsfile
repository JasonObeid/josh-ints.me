pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
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
        sh '''sudo rm -r prod
sudo cp -r dist prod'''
      }
    }

  }
}