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

  }
}