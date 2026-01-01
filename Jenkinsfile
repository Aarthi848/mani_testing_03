pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Aarthi848/mani_testing_03.git'
            }
        }
        stage('Run Demo') {
            steps {
                sh 'python demo.py'
            }
        }
    }
}