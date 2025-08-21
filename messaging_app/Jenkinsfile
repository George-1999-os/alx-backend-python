pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/George-1999-os/alx-backend-python.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh '. venv/bin/activate && pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml'
            }
        }

        stage('Archive results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
