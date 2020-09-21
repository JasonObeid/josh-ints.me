pipeline {
  agent {
    node {
      label 'node'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'npm run build'
      }
    }

  }
}
