# Machine-learning-Project
Requirement 

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


creating conda environment
'''
conda create -p venv python==3.7 -y

'''

conda activate venv/


'''

pip install -r requirements.txt

'''
To add files to git

'''
git add . ----> adding all files
git add file ----> add one file

'''

Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check git status 
'''
git status

'''

To check all versions maintained by git
'''
git log

'''

To create a version/commit all changes by git
'''
git commit -m 'message'

'''

To send vesrion/changes to github
'''
git push origin main

'''

To check remote url
'''
git remote -v

'''

To set up CI/CD pipeline in heroku we need 3 information

1. HEROKU_email
2. HEROKU_API_KEY
3. HEROKU_APP_NAME

Build Docker image
'''
docker build -t <image_name>:<tag_name> .

'''
Note: Image name for docker must be lower case

To list docker images
'''
docker images

'''

To run docker image
'''
docker run -p 5000:5000 -e PORT=5000 imgae id

'''

To check running containers in docker
'''
docker ps

'''

To stop docker container
'''
docker stop <container_id>

'''

'''
python setup.py install

'''