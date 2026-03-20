# Day 5 - AWS EC2 & SSH Connection

What I Did?

		Launched an AWS EC2 instance (Ubuntu Server)
		Created and downloaded a key pair (.pem file)
		Connected to the server using SSH from my local machine
		Installed Git on the EC2 instance
		Cloned my GitHub repository on the server
		Fixed GitHub authentication issue using SSH keys


SSH Connection: 
	Commands used:

		```bash
		ssh -i ~/devops-key.pem ubuntu@<public-ip>

Setup on EC2;

	Installed Git:
		sudo apt update
		sudo apt install git -y
	
	Cloned repository:
		git clone https://github.com/username/devops-learning-journey.git
		cd devops-learning-journey

	Problem Faced:
	While pushing code:
		git push
	Error:
		Password authentication is not supported

	Solution (SSH Authentication):
		1. Generated SSH key on EC2- 'ssh-keygen'
		2. Copied public key- 'cat ~/.ssh/id_abc.pub'
		3. Added key to GitHub: GitHub → Settings → SSH Keys → Added new key
		4. Changed remote URL: 'git remote set-url origin git@github.com:username/file.git'
		5. Tested connection: 'ssh -T git@github.com'
		6. Successfully pushed code: 'git push'

Key Learnings:

	Managing remote cloud servers via SSH
	Working across local and remote environments
	Handling Git authentication securely using SSH keys
	Debugging real-world issues in a cloud environment
	
Key Takeaway:

	This task involved working with a cloud server (AWS EC2) and securely connecting it to GitHub using SSH, which is a core DevOps workflow.
