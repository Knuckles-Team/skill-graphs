[Skip to content](https://www.tecmint.com/setting-up-linux-for-ai-development/#content "Skip to content")
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
Menu
  * [Learn Linux](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/ "Start Learning Linux")
  * [Linux Distros](https://www.tecmint.com/best-linux-distributions/ "Linux Distributions")
    * [Linux Distros for Beginners](https://www.tecmint.com/best-linux-distributions-for-beginners/)
    * [Linux Distros for Experts](https://www.tecmint.com/linux-distro-for-power-users/ "Widely Used Distros")
    * [New Linux Distros](https://www.tecmint.com/new-linux-distributions/)
    * [Linux Server Distros](https://www.tecmint.com/10-best-linux-server-distributions/)
    * [Secure Linux Distros](https://www.tecmint.com/best-security-centric-linux-distributions/)
    * [CentOS Alternatives](https://www.tecmint.com/centos-alternative-distributions/ "CentOS Alternative Distros")
    * [RedHat Distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat Based Distros")
    * [Debian Distributions](https://www.tecmint.com/debian-based-linux-distributions/ "Debian Based Distros")
    * [Ubuntu Distributions](https://www.tecmint.com/ubuntu-based-linux-distributions/ "Ubuntu Based Distros")
    * [Arch Linux Distros](https://www.tecmint.com/arch-based-linux-distributions/ "Arch Linux Based Distros")
    * [Rolling Linux Distros](https://www.tecmint.com/best-rolling-release-linux-distributions/)
    * [KDE Linux Distros](https://www.tecmint.com/best-linux-distributions-for-kde-plasma/ "KDE Based Distros")
    * [Linux Distros for Old PC](https://www.tecmint.com/linux-distributions-for-old-computers/ "Linux Distros for Older Computers")
    * [Linux Distros for Kids](https://www.tecmint.com/best-linux-distributions-for-kids/)
    * [Linux Distributions for Students](https://www.tecmint.com/linux-distros-students/)
    * [Linux Distros for Windows](https://www.tecmint.com/best-alternative-linux-distributions-for-windows-users/)
  * [Commands](https://www.tecmint.com/category/linux-commands/ "Linux Commands")
    * [A – Z Linux Commands](https://www.tecmint.com/linux-commands-cheat-sheet/)
    * [100+ Linux Commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands")
  * [Tools](https://www.tecmint.com/category/top-tools/ "Best Linux Software")
  * [Pro Courses](https://www.tecmint.com/setting-up-linux-for-ai-development/ "Linux Online Courses")
    * [Bash Scripting](https://pro.tecmint.com/learn-bash-scripting/ "Bash Scripting for Beginners")
    * [Learn Linux](https://pro.tecmint.com/learn-linux/ "Master Linux in 7 Days")
    * [AI for Linux](https://pro.tecmint.com/ai-for-linux/ "AI for Linux Course")
    * [RHCSA Certification](https://pro.tecmint.com/rhcsa-certification-course/ "RHCSA Certification Course")
    * [RHCE Certification](https://pro.tecmint.com/rhce-certification-course/ "RHCE Certification Course")
    * [LFCS Certification](https://pro.tecmint.com/lfcs-certification-course/ "LFCS Certification Course")
  *     * [RHCSA Exam](https://www.tecmint.com/rhcsa-exam-reviewing-essential-commands-system-documentation/ "RHCSA Certification eBook")
    * [RHCE Exam](https://www.tecmint.com/how-to-setup-and-configure-static-network-routing-in-rhel/ "RHCE Certification eBook")
    * [LFCS Exam](https://www.tecmint.com/sed-command-to-create-edit-and-manipulate-files-in-linux/ "LFCS Certification eBook")
    * [LFCE Exam](https://www.tecmint.com/installing-network-services-and-configuring-services-at-system-boot/ "LFCE Certification eBook")
    * [LFCA Exam](https://www.tecmint.com/understanding-linux-operating-system/ "LFCA Certification eBook")
    * [Ansible Exam](https://www.tecmint.com/understand-core-components-of-ansible/ "Ansible Certification eBook")
  * [About](https://www.tecmint.com/who-we-are/)
    * [Contact](https://www.tecmint.com/contact-us/ "Contact Us")
    * [Hiring](https://www.tecmint.com/hiring/ "Write for Us")
    * [Newsletter](https://www.tecmint.com/subscribe-to-blog/ "Linux Weekly Newsletter")
    * [Testimonials](https://www.tecmint.com/testimonials/)
    * [Donate](https://www.tecmint.com/donate-to-tecmint/ "Support TecMint")
    * [Advertise](https://www.tecmint.com/advertise/ "TecMint Sponsorship Opportunities")
    * [Submit Article Request](https://www.tecmint.com/submit-article-request/)
    * [Suggest an Update](https://www.tecmint.com/suggest-an-update/)


[](https://www.tecmint.com/setting-up-linux-for-ai-development/)
In the previous article, we introduced the [basics of AI](https://www.tecmint.com/ai-for-linux-users/ "What is AI for Linux") and how it fits into the world of Linux. Now, it’s time to dive deeper and set up your Linux system to start building your first AI model.
Whether you’re a complete beginner or have some experience, this guide will walk you through installing the essential tools you need to get started on [Debian-based systems](https://www.tecmint.com/debian-based-linux-distributions/ "Debian-based Linux Distributions").
#### System Requirements for Ubuntu 24.04
Before we begin, let’s make sure your system meets the minimum requirements for AI development.
  * **Operating System** : Ubuntu 24.04 LTS (or newer).
  * **Processor** : A 64-bit CPU with at least 2 cores (**Intel Core i5** or **AMD Ryzen 5** or better recommended for smooth performance).
  * **RAM** : Minimum 4 GB of RAM (8 GB or more recommended for more intensive AI models).
  * **Storage** : At least 10 GB of free disk space (SSD is highly recommended for faster performance).
  * **Graphics Card (Optional)** : A dedicated GPU (**NVIDIA** recommended for deep learning) with at least 4 GB of **VRAM** if you plan to use frameworks like **TensorFlow** or **PyTorch** with GPU acceleration.


## Step 1: Install Python on Ubuntu
**Python** is the most popular programming language for AI development, due to its simplicity, powerful, and huge library of tools and frameworks.
Most Linux systems come with **Python** pre-installed, but let’s make sure you have the latest version. If **Python** is installed, you’ll see something like `Python 3.x.x`.
```
python3 --version

```

If **Python** is not installed, you can easily install it using the package manager.
```
sudo apt update
sudo apt install python3

```

Next, you need to install pip (python package manager), which will help you install and manage Python libraries.
```
sudo apt install python3-pip

```

## Step 2: Install Git on Ubuntu
[Git](https://www.tecmint.com/git-basics/ "Learn the Basics of Git") is a version control tool that allows you to track changes in your code and collaborate with others, which is essential for AI development because many AI projects are shared on platforms like **GitHub**.
```
sudo apt install git

```

Verify the installation by typing:
```
git --version

```

You should see something like `git version 2.x.x`.
![Install Git in Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/01/Install-Git-in-Ubuntu.png)Install Git in Ubuntu
## Step 3: Set Up a Virtual Environment in Ubuntu
A virtual environment helps you manage your projects and their dependencies in isolation, which means you can work on multiple projects without worrying about conflicts between different libraries.
First, make sure you have the `python3-venv` package installed, which is needed to create a virtual environment.
```
sudo apt install python3-venv

```

Next, you need to create a new directory for your project and set up a virtual environment:
```
mkdir my_ai_project
cd my_ai_project
python3 -m venv venv
source venv/bin/activate

```

After running the above commands, your terminal prompt should change, indicating that you’re now inside the virtual environment.
![Setup Python Virtual Environment](https://www.tecmint.com/wp-content/uploads/2025/01/Setup-Python-Virtual-Environment.png)Setup Python Virtual Environment
## Step 4: Install AI Libraries on Ubuntu
Now that you have **Python** , **Git,** and **Virtual Environment** set up, it’s time to install the libraries that will help you build AI models.
Some of the most popular libraries for AI are **TensorFlow** , **Keras** , and **PyTorch**.
### Install TensorFlow in Ubuntu
**TensorFlow** is an open-source library developed by **Google** that is widely used for machine learning and AI projects.
```
pip3 install tensorflow

```
![Install TensorFlow in Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/01/Install-TensorFlow-in-Ubuntu.png)Install TensorFlow in Ubuntu
### Install Keras in Ubuntu
**Keras** is a high-level neural networks API, written in Python, that runs on top of **TensorFlow**.
```
pip3 install keras

```
![Install Keras in Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/01/Install-Keras-in-Ubuntu.png)Install Keras in Ubuntu
### Install PyTorch in Ubuntu
**PyTorch** is another popular AI library, especially for deep learning.
```
pip3 install torch

```
![Install PyTorch in Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/01/Install-PyTorch-in-Ubuntu.png)Install PyTorch in Ubuntu
## Step 5: Building Your First AI Model
Now that your system is ready, let’s build a simple AI model called a **neural network** using **TensorFlow** and **Keras** to classify handwritten digits from the famous **MNIST** dataset.
Create a new Python file called `first_ai_model.py` and open it in your [favorite text editor](https://www.tecmint.com/linux-command-line-editors/ "My Favorite Editors for Linux").
```
sudo nano first_ai_model.py

```

At the top of the file, add the following imports to import the necessary libraries:
```
import tensorflow as tf
from tensorflow.keras import layers, models

```

Next, load the **MNIST** dataset, which contains 60,000 images of handwritten digits (0-9) to train our model.
```
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

```

Preprocess the data to normalize the images to values between 0 and 1 by dividing by 255.
```
train_images, test_images = train_images / 255.0, test_images / 255.0

```

Build the model by creating a simple neural network with one hidden layer.
```
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)
])

```

Compile the model by specifying the optimizer, loss function, and metrics for evaluation.
```
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

```

Train the model using the training data.
```
model.fit(train_images, train_labels, epochs=5)

```

Finally, test the model on the test data to see how well it performs.
```
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

```

## Step 6: Run the AI Model
Once you’ve written the code, save the file and run it in your terminal:
```
python3 first_ai_model.py

```

The model will begin training, and after 5 epochs, it will display the test accuracy. The higher the accuracy, the better the model’s performance.
![Run AI Model](https://www.tecmint.com/wp-content/uploads/2025/01/Run-the-AI-Model.png)Run AI Model
Congratulations, you’ve just built your first AI model!
##### Conclusion
In this guide, we covered how to set up your Linux system for AI development by installing **Python** , **Git** , and essential AI libraries like **TensorFlow** , **Keras** , and **PyTorch**.
We also walked through building a simple neural network to classify handwritten digits. With these tools and knowledge, you’re now ready to explore the exciting world of AI on Linux!
Stay tuned for more articles in this series, where we’ll dive deeper into AI development techniques and explore more advanced topics.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Jellyfin: The Ultimate Free Media Server for Linux Users](https://www.tecmint.com/jellyfin-free-media-server-for-linux/)
Next article:
[8 Best Free Courses to Learn Large Language Models (LLMs)](https://www.tecmint.com/free-llm-courses/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/setting-up-linux-for-ai-development/#respond)** or
## Related Posts
[![Whisper AI Speech to Text on Linux](https://www.tecmint.com/wp-content/uploads/2025/03/Whisper-AI-Speech-to-Text-on-Linux.png)](https://www.tecmint.com/whisper-ai-audio-transcription-on-linux/ "Running Whisper AI for Real-Time Speech-to-Text on Linux")
[![Linux Tools for AI Development](https://www.tecmint.com/wp-content/uploads/2025/02/Linux-Tools-for-AI-Development.webp)](https://www.tecmint.com/linux-tools-for-ai-development/ "Best Linux Tools for AI Development in 2025")
[![Install DeepSeek in Linux](https://www.tecmint.com/wp-content/uploads/2025/01/Install-DeepSeek-Locally-in-Linux.webp)](https://www.tecmint.com/run-deepseek-locally-on-linux/ "How to Install DeepSeek Locally with Ollama LLM in Ubuntu 24.04")
[![GPT4All AI Editing in OnlyOffice](https://www.tecmint.com/wp-content/uploads/2025/01/gpt4all-ai-editing-in-onlyoffice.webp)](https://www.tecmint.com/gpt4all-ai-editing-in-onlyoffice/ "AI Document Editing: Connect GPT4All to ONLYOFFICE on Ubuntu")
[![Free LLM Courses](https://www.tecmint.com/wp-content/uploads/2025/01/Free-LLM-Courses.webp)](https://www.tecmint.com/free-llm-courses/ "8 Best Free Courses to Learn Large Language Models \(LLMs\)")
[![AI for Linux Users](https://www.tecmint.com/wp-content/uploads/2025/01/AI-for-Linux-Users.webp)](https://www.tecmint.com/ai-for-linux-users/ "A Beginner’s Guide to Artificial Intelligence for Linux Users")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/setting-up-linux-for-ai-development/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/setting-up-linux-for-ai-development/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=1169308278425711&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
