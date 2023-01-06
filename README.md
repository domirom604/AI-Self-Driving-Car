<h1 align="center"> <strong> AI-Self-Driving-Car </strong> </h1>

<h5 align="center"> Easy to use and helpful in advanced simulations </h5>
<img
  src="https://github.com/domirom604/AI-Self-Driving-Car/blob/main/logo.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 100px">

## Features
<ul>
  <li>Real simulation of physics</li>
  <li>Three application modes:
    <ul>
      <li>Casual game</li>
      <li>Study and experimental mode</li>
      <li>Mode of testing learned model</li>
    </ul>
  </li>
  <li>Well-adjusted genetic algorithm</li>
  <li>Algorithm can be adapted for any simulation map</li>
  <li>Ability to adjust the accuracy of the simulation</li>
</ul>

## Model
<ul>
  <li>Input:
    <ul>
      <li>Information from left sensor</li>
      <li>Information from middle sensor</li>
      <li>Information from right sensor</li>
    </ul>
  </li>
</ul>

<img
  src="https://github.com/domirom604/AI-Self-Driving-Car/blob/main/topology.png"
  alt="Alt text"
  style="display: inline-block; margin: 0 auto; max-width: 100px">
  
<ul>
  <li>Output:
    <ul>
      <li>Turn left</li>
      <li>Turn right</li>
    </ul>
  </li>
</ul>

## Usage

<details>
    <summary><strong>Installation</strong> (click to expand)</summary>
       <ul>
        <li> Python >= 3.8 </li>
        <li> KerasGA = 1.0.0 </li>
        <li> Keras >= 2.11.0 </li>
        <li> Tensorflow >= 2.11.0 </li>
        <li> Basic libraries like: pandas, numpy, pillow </li>
       </ul>
         Then, clone the repo and install the project with:
         
          $ git clone https://github.com/domirom604/AI-Self-Driving-Car
          $ cd AI-Self-Driving-Car
          $ pip install -e .
         
      
</details>
         
<details>
    <summary><strong>Configuration</strong> (click to expand)</summary>
       <p>User may configure several parameters like:</p>
        <ul>
        <li>velocity of car/simulation in Car Class</li>
          For example:
          self.velocity = 1
        <li>length of sensors in Car Class</li>
          For example:
          sensor_length = 120     
        <li>application mode in Evolve and Main Class
            <ul>
              <li>Casual game by runing main file</li>
                Main file configuration:
                game = Play(control="player",model=None)
              <li>Study and experimental mode by runing evolve file</li>
                Main file configuration:
                game = Play(control="keras",model=None)
               <li>Mode of testing learned model by runing main file</li>
                Main file configuration:
                game = Play(control="keras",model=keras.models.load_model('model_15.h5'))
            </ul>
         </li>
      </ul>
  
</details>

<details> 
    <summary> <strong>Evolving</strong> (click to expand)</summary> 
       <p> To detect obstacles by car Genetic Algorithm has been implemented</p>
       <p> User may change several parameters in model:</p>
          <ul>
            <li> hidden layer and input and output parameters</li>
               <p>def model(): </p>
                   <p>   model = keras.models.Sequential() </p>
                   <p>   model.add(keras.layers.Dense(3,activation='relu',input_shape=(3,))) </p>
                   <p><strong>    model.add(keras.layers.Dense(5, activation='relu'))</strong> </p>
                   <p>    model.add(keras.layers.Dense(2, activation='sigmoid')) </p>
                   <p>return model </p>
            <li> saving model after reaching exact score progress </li>     
         </ul>
</details>
         
<details>
     <summary><strong>References</strong> (click to expand)</summary>
       <ul>
        <li>https://pypi.org/project/KerasGA/</li>
        <li>https://www.tensorflow.org/api_docs/python/tf/keras/Model#predict</li>
        <li>https://www.pygame.org/docs/</li>
        <li>https://keras.io/guides/sequential_model/</li>
      </ul>
</details>
