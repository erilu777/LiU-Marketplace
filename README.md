# LiU Marketplace - Startup Idea & Bachelor Thesis Project
<p>
    LiU Marketplace is a platform for students to buy and sell used items. It utilizes Microsoft's Azure AD for authentication (Single Sign-On (SSO)) to securely manage trusted users within the student community. It is a a secure digital marketplace specifically for Linköping University (LiU) students to address security and trust concerns in existing online marketplaces. 
</p>


## Getting Started

### Prerequisites
- Python 3.x
- Vue.js and npm

### Clone the repository

### Setting Up the Environment

#### 1. Python Backend Setup - in root directory

a. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate
```

b. Install the required packages (inside the virtual environment and root directory):
```bash
pip install -r requirements.txt
```

#### 2. Vue.js Frontend Setup - in frontend directory

a. Navigate to the frontend directory:
```bash
cd client
```

b. Install the required packages:
```bash
npm install
```

### Running the Application

#### 1. Python Backend  

a. Navigate to the backend directory:
```bash
cd server
```

b. Run the Flask server:
```bash
python main.py
```

#### 2. Vue.js Frontend

a. Navigate to the frontend directory:
```bash
cd client
```

b. Run the Vue.js application:
```bash
npm run serve
```

## Important Notes - How to login

### Login with Microsoft Azure AD - For Linköping University students

1. Press the big blue button to login with SSO from Linköping University.
2. You will be redirected to the Microsoft Azure AD login page.
3. Enter your Linköping University email and password.
4. You will be redirected back to the LiU Marketplace.

### Login WITHOUT Microsoft Azure AD - For everyone else

1. Type in whatever you want in the "liu_id" field under the big blue button.
2. Press "Logga in"
3. You will be redirected in to the LiU Marketplace.

<!-- 
## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
-->