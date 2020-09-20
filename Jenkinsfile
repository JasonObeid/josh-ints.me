pipeline {
  agent none
  stages {
    stage('build') {
      steps {
        sh 'npm run build'
      }
    }

    stage('deploy') {
      steps {
        sh '''sudo systemctl restart nginx
sudo systemctl restart josh'''
      }
    }

  }
}