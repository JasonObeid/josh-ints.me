pipeline {
    agent any
    stages {
        stage('Example Build') {
            when {
                branch 'master'
            }
            steps {
                sh 'cd src'
                sh 'npm install'
                sh 'npm run build'
            }
            when {
                branch 'dev'
            }
            steps {
                sh 'cd src'
                sh 'npm install'
                sh 'npm run build'
            }
        }
    }
}
