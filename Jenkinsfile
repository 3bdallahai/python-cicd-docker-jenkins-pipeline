pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
        CONTAINER_NAME = "my-python-container"
        LOG_LEVEL = "INFO"
    }

    stages {

    stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/3bdallahai/python-cicd-docker-jenkins-pipeline'
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Cleanup Old Container') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                  --name $CONTAINER_NAME \
                  -e LOG_LEVEL=$LOG_LEVEL \
                  $IMAGE_NAME:latest
                '''
            }
        }

        stage('Extract Logs') {
            steps {
                sh '''
                docker cp $CONTAINER_NAME:/app/logs ./logs || true
                cat logs/app.log || true
                '''
            }
        }

        stage('Fail on Errors in Logs') {
            steps {
                sh '''
                if grep -i "error" logs/app.log; then
                    echo "Error found in logs. Failing pipeline."
                    exit 1
                fi
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'logs/app.log', allowEmptyArchive: true
        }
    }
}
