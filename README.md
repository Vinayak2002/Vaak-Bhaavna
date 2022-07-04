<H1 align =center>VAAK BHAAVNA </H1>
<p align =center>" वाक् भावना "</p>
<p align =center>"आवाज में छुपी हुई भावना को जानना है जरूरी"</p>
<p align="center">
  <img width="200" src="https://github.com/Vinayak2002/Vaak-Bhaavna/blob/main/images/logo.jpeg" alt="Material Bread logo">
</p>


Vaak-Bhaavna is a website which tells us about emotions as well as gender of the speaker with the help of the speech input which the person gives and based on its speech-emotion recognition technique.It can classify emotion into 3 classes: Positive,Negative and Neutral. The emotions which can be classified into happy, sad, fear, angry, disgust, neutral and surprise.

# Features - 

* ANALYSIS - Analyzing the wave form of the audio given as input using MFCCs and Mel-log-spectrogram.
* GENDER PREDICTION - Predicting speaker gender that is whether the speaker is male or female with the help of speech given as input.
* EMOTION PREDICTION - Predicting speaker emotion with the help of speech given as input.
  * 3 emotion: Positive, Negative, Neutral
  * 6 emotion:Happy, sad, Angry, Fear, Neutral, Surprise
  * 7 emotion: Disugust, Happy, sad, Angry, Fear, Neutral, Surprise

# Technologies used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br />
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) <br />
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) <br />
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) <br />
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) <br />
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) <br />
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) <br />

# How to use - 
The web-application predicts the emotion from the audio input given. It can also predict the gender of the speaker. You can either upload an audio file you can record the live audio and download it in .wav format


# Website layout
 <p align ="center" >
  <img  width="700" src="https://github.com/Vinayak2002/Vaak-Bhaavna/blob/main/images/site.gif" alt="Material Bread logo">
  </p>

# Test Cases-

 * case - 1 :
 
 https://user-images.githubusercontent.com/76607471/177053274-03896a05-9813-4c09-9a13-4c36b1230a0b.mp4
 
 <p align ="center" >
  <img  width="700" src="https://github.com/Vinayak2002/Vaak-Bhaavna/blob/main/images/male.gif" alt="Material Bread logo">
  </p>
  
 * OUTPUT- 
 
  
  * case - 2 :
  
  https://user-images.githubusercontent.com/76607471/177053298-cd36a032-5e00-4e00-a68d-ffb7c03cc548.mp4
  
 <p align ="center" >
  <img  width="700" src="https://github.com/Vinayak2002/Vaak-Bhaavna/blob/main/images/female.gif" alt="Material Bread logo">
  </p>

 * OUTPUT- 

## Instructions for running the application

Clone the repository:
```zsh
git clone https://github.com/Vinayak2002/Vaak-Bhaavna.git
```

Create a new virtual environment from the yml file:
```zsh
conda env create -f environment.yml
```

Activate the virtual environment :
```zsh
conda activate FinalWebsite
```

Install all required python packages :
```zsh
pip install -r requirements.txt
```

Install the node package:
```zsh
npm install ffmpeg
```

Add the Secret Key in the settings.py file.

Run the application :
```python
python manage.py runserver
```
---

Made with :heart: at IIIT Naya Raipur .
