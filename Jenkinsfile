pipeine{
    agent any

    environment {
        DOCKER_IMAGE = ""
    }

    stages{
        
        stage('Checkout'){
            steps{
                git branch: 'main',
                    url: ''
            }
        }

        stage('Build'){
            steps{
                sh 'docker build -t flask-rest-api:latest .'
            }
        }
        stage('Test'){
            steps{
                sh 'docker run --rm $IMAGE_NAME:latest python -m pytest tests/ || echo "No Test Found"'
            }
        }

        stage('Push'){
            steps{

            }
        }

        stage('Deploy'){
            steps{

            }
        }



    }



    post {
        success {
            echo 'Deployed successfully!'
        }
        failure {
            echo 'Pipeline failed — check the logs above.'
        }
    }
}