pipeline {
    agent any
    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        S3_BUCKET = 'titanic-dataset'
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/poornikabonam/aws.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Preprocess Data') {
            steps {
                sh 'python data_preprocessing.py'
            }
        }

        stage('Define and Deploy Pipeline') {
            steps {
                sh 'python pipeline_definition.py'
            }
        }
    }

    triggers {
        pollSCM('H/15 * * * *') // Polls every 15 minutes
    }
}
