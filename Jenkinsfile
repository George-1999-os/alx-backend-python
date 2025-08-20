pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/George-1999-os/alx-backend-python.git',
                    credentialsId: 'github-credentials'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip3 install -r messaging_app/requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml'
            }
        }

        stage('Test Report') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
