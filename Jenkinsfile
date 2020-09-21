pipeline {
  agent {
    node {
      label 'node'
    }

  }
  stages {
    stage('build') {
      steps {
        if (env.BRANCH_NAME == 'master') {
          sh 'cd src'
          sh 'npm install'
          sh 'npm run build'
        } else {
          sh 'cd src'
          sh 'npm install'
          sh 'npm run build'
        }
      }
    }

  }
}
