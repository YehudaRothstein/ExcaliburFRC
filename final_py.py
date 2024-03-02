{% extends "base.html" %}
{% block title %}Scout{% endblock %}
{% block content %}
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='Scout.css') }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    body {
      text-align: center;
      background-color: #012265;
    }
    p, h2, h4, button, input, label, h6 {
        color: #d3af37;
    }
    input[id="submit"]{
        background-color: #d3af37;
        color: #012265;
        border: none;
    }
    input[name="scouter_name"], input[name="submit"], input[name="team"], input[name="qual_number"], input[name = "manualClimbTime"] , select, textarea {
        background-color: #d3af37;
        color: #012265;
    }
    input[id="counter2"], input[id="counter1"],  input[id="counter7"] , input[id="counter3"],input[id="counter67"],input[id="counter13"], input[id="counter4"], input[id="counter5"], input[id="counter6"], input[id="counter8"] {
        background-color: #012265;
        color: #d3af37;
        border: none;
    }

    .button-set {
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 150px;  /* Set the maximum width for the button set */
        margin: 0 auto;    /* Center the button set */
    }

    .button-set button, button {
        width: 100px;  /* Adjust the width of the +/- buttons */
        height: 30px;
        font-size: 16px;  /* Adjust the font size of the buttons */
        background-color: #d3af37;
        color: #012265;
        border: none;
    }

    .button-set input {
        width: 40px;  /* Adjust the width of the counter input */
        height: 30px;
        text-align: center;
        font-size: 16px;  /* Adjust the font size of the counter input */
    }

</style>

<head>
    <link rel="stylesheet" href="base.css">
    <title></title>
</head>

<form id="scoutForm" action="https://yehudarothstein.pythonanywhere.com/process_form" method="post" onsubmit="submitForm(event)">
    <p>Your name:</p>
    <label>
        <input type="text" name="scouter_name">
    </label>

    <p>Qual Number:</p>
    <label>
        <input type="number" name="qual_number">
    </label>

    <p>Team:</p>
    <label>
        <input type="number" name="team">
    </label>

    <p>Select Alliance:</p>
    <label for="alliance-select"></label>
    <select name="Alliances Options" id="alliance-select">
        <option value="">Please choose an alliance</option>
        <option value="Blue">Blue</option>
        <option value="Red">Red</option>
    </select>

    <script>
    function updateCounter(change, counterId, category) {
        let counterValue = parseInt(document.getElementById(counterId).value);
        if (counterId === 'counter8' && counterValue >= 3 && change > 0) {
            // If the counter is for "Trap" and it's already at 3, don't increment it
            return;
        }
        counterValue = Math.max(0, counterValue + change);
        document.getElementById(counterId).value = counterValue;
        let totalCounterId = 'totalCounter' + category;
        let totalCounterValue = parseInt(document.getElementById(totalCounterId).value);
        totalCounterValue = Math.max(0, totalCounterValue + change);
        document.getElementById(totalCounterId).value = totalCounterValue;
    }
    </script>

 </script>

    <br>
    <br>
    <hr>
    <h2>Autonomous</h2>

    <h6>AMP:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter1', 'Autonomous')">-</button>
        <label for="counter1"></label><input type="text" id="counter1" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter1', 'Autonomous')">+</button>
    </div>
        <br>
    <h6>Speaker:</h6>
    <div class="button-set">

        <button onclick="event.preventDefault(); updateCounter(-1, 'counter2', 'Autonomous')">-</button>
        <label for="counter2"></label><input type="text" id="counter2" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter2', 'Autonomous')">+</button>
    </div>
        <br>
    <div class="checkbox-container">
        <input type="checkbox" id="vehicle4" name="Another checkbox" value="Another checkbox">
        <label for="vehicle4">Left Robot Starting Zone</label>
    </div>
        <br>
    <div class="checkbox-container">
        <input type="checkbox" id="vehicle2" name="Another checkbox" value="Another checkbox">
        <label for="vehicle2">Arrived To the middle</label>
    </div>
        <br>

    <h6>Collected parts from the middle:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter3', 'Autonomous')">-</button>
        <label for="counter3"></label><input type="text" id="counter3" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter3', 'Autonomous')">+</button>
    </div>
        <br>
<hr>
    <h2>Teleop</h2>

    <h6>AMP:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter4', 'Teleop')">-</button>
        <label for="counter4"></label><input type="text" id="counter4" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter4', 'Teleop')">+</button>
    </div>
    <br>

    <h6>Speaker:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter5', 'Teleop')">-</button>
        <label for="counter5"></label><input type="text" id="counter5" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter5', 'Teleop')">+</button>
    </div>
    <br>
    <h6>Pins:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter6', 'Teleop')">-</button>
        <label for="counter6"></label><input type="text" id="counter6" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter6', 'Teleop')">+</button>
        </div>
            <br>
                <h6>Shooting To Speaker Misses:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter13', 'Teleop')">-</button>
        <label for="counter13"></label><input type="text" id="counter13" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter13', 'Teleop')">+</button>
        </div>
            <br>
                            <h6>Placing At AMP Misses:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter67', 'Teleop')">-</button>
        <label for="counter67"></label><input type="text" id="counter67" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter67', 'Teleop')">+</button>
        </div>
            <br>
<hr>
    <h2>EndGame</h2>
    <title>Timer Climb</title>
          <style>
            #timerDisplay {
              font-size: 24px;
              margin-top: 10px;
            }
          </style>
      <style>
        #timerDisplay {
          font-size: 17px;
          margin-top: 10px;
        }

      </style>

<h6>Choose Climb Time Entry Method:</h6>
<select id="climbChoice" name="climbChoice" onchange="toggleClimbEntry()">
    <option value="timer" selected>Use Timer</option>
    <option value="manual">Manual Entry</option>
</select>
<br>
<div id="manualClimbContainer" style="display: none;">
    <h6>Manual Climb Time (seconds):</h6>
    <input type="number" id="manualClimbTime" name="manualClimbTime" placeholder="Enter climb time" step="1">
</div>
<br>
<h6>Climb timer:</h6>
<button id="timerButton" onclick="toggleTimer(event)">Start Timer</button>
<button id="resetTimerButton" onclick="resetTimer(event)">Reset Timer</button>

<p id="timerDisplay">Timer: 0.00 seconds</p>

<input type="checkbox" id="end6" name="Another checkbox" value="Another checkbox"> <label>Didn't Climb</label>
<br>
<br>
<script>
    function toggleDidntClimb() {
        const didntClimbCheckbox = document.getElementById('end6');
        didntClimbCheckbox.checked = !didntClimbCheckbox.checked; // Toggle the checkbox value
    }

    let timer;
    let isTimerRunning = false;
    let milliseconds = 0;

function toggleClimbEntry() {
    const climbChoice = document.getElementById('climbChoice').value;
    const manualClimbContainer = document.getElementById('manualClimbContainer');
    const timerDisplay = document.getElementById('timerDisplay');
    const timerButton = document.getElementById('timerButton');
    const resetTimerButton = document.getElementById('resetTimerButton');

    if (climbChoice === 'manual') {
        manualClimbContainer.style.display = 'block';
        timerDisplay.style.display = 'none';
        timerButton.style.display = 'none';
        resetTimerButton.style.display = 'none';
    } else {
        manualClimbContainer.style.display = 'none';
        timerDisplay.style.display = 'block';
        timerButton.style.display = 'inline-block';
        resetTimerButton.style.display = 'inline-block';
    }
}

    function toggleTimer(event) {
        event.preventDefault();
        const manualClimbContainer = document.getElementById('manualClimbContainer');
        const timerDisplay = document.getElementById('timerDisplay');
        const timerButton = document.getElementById('timerButton');

        if (isTimerRunning) {
            clearInterval(timer);
            timerButton.innerText = 'Start Climb';
        } else {
            if (document.getElementById('climbChoice').value === 'manual') {
                const manualClimbTime = parseFloat(document.getElementById('manualClimbTime').value) || 0;
                alert('Manual Climb Time: ' + manualClimbTime + ' seconds');
            } else {
                timer = setInterval(updateTimer, 10);
                timerButton.innerText = 'Stop Climb';
            }
        }

        isTimerRunning = !isTimerRunning;
    }

    function resetTimer(event) {
        event.preventDefault();
        if (isTimerRunning) {
            clearInterval(timer);
            isTimerRunning = false;
            document.getElementById('timerButton').innerText = 'Start Climb';
        }
        milliseconds = 0;
        document.getElementById('timerDisplay').innerText = 'Timer: 0.00 seconds';
    }

    function updateTimer() {
        milliseconds += 10;
        const seconds = (milliseconds / 1000).toFixed(2);
        document.getElementById('timerDisplay').innerText = 'Timer: ' + seconds + ' seconds';
    }
</script>

    <h6>Trap:</h6>
    <div class="button-set">
        <button onclick="event.preventDefault(); updateCounter(-1, 'counter8', 'EndGame')">-</button>
        <label for="counter8"></label><input type="text" id="counter8" value="0" readonly>
        <button onclick="event.preventDefault(); updateCounter(1, 'counter8', 'EndGame')">+</button>
    </div>
        <br>


    <div class="checkbox-container">
        <label for="vehicle6"></label><input type="checkbox" id="vehicle6" name="Another checkbox" value="Another checkbox">
        <label for="vehicle2">Climbed with another robot</label>
    </div>
          <br>
      <h4> From Where Did The Robot Shoot:</h4>
<input type="checkbox" id="end1" name="Another checkbox" value="Another checkbox"> <label for="vehicle2">Close to the speaker</label>
<br>
<input type="checkbox" id="end2" name="Another checkbox" value="Another checkbox"> <label for="vehicle2">From Our Area</label>
<br>
<input type="checkbox" id="end3" name="Another checkbox" value="Another checkbox"> <label for="vehicle2">From the Middle</label>
<br>
<h4>Comments:</h4>
<label>
    <textarea name="comments" rows="4" cols="50"></textarea>
</label>
<br>
<br>

<script>
function submitForm(event) {
    event.preventDefault(); // Prevent the traditional form submission

    // Form validation and data preparation
    const timerDisplayText = document.getElementById('timerDisplay').innerText;
    const climbChoice = document.getElementById('climbChoice').value;
    let climbTimerSeconds;

    if (climbChoice === 'manual') {
        climbTimerSeconds = parseFloat(document.getElementById('manualClimbTime').value) || 0;
    } else {
        climbTimerSeconds = parseFloat(timerDisplayText.split(":")[1]) || 0;
    }

    const validTeams = [
        1574, 1576, 1577, 1580, 1690, 1942, 2230, 2630, 2679, 3065, 3083, 3211,
        3316, 3339, 4319, 4320, 4338, 5135, 5654, 5715, 5990,5951, 6230, 6738, 6740,
        6741, 7067, 7177, 8175, 9303, 9738, 9740, 9741
    ];

    const data = {
        scouter_name: document.querySelector('input[name="scouter_name"]').value,
        qual_number: document.querySelector('input[name="qual_number"]').value,
        team: document.querySelector('input[name="team"]').value,
        alliance: document.querySelector('select[name="Alliances Options"]').value,
        auto_amp: document.getElementById('counter1').value,
        auto_speaker: document.getElementById('counter2').value,
        auto_collected_parts_from_middle: document.getElementById('counter3').value,
        left_robot_starting_zone: document.getElementById('vehicle4').checked,
        arrived_to_middle: document.getElementById('vehicle2').checked,
        teleop_amp: document.getElementById('counter4').value,
        teleop_speaker: document.getElementById('counter5').value,
        teleop_pins: document.getElementById('counter6').value,
        speaker_misses: document.getElementById('counter13').value,
        amp_misses: document.getElementById('counter67').value,
        endgame_trap: document.getElementById('counter8').value,
        climb_timer_seconds: climbTimerSeconds,
        climbed_with_another_robot: document.getElementById('vehicle6').checked,
        close_to_speaker: document.getElementById('end1').checked,
        from_our_area: document.getElementById('end2').checked,
        from_the_middle: document.getElementById('end3').checked,
        climbed: document.getElementById('end6').checked,
        comments: document.querySelector('textarea[name="comments"]').value,
    };

   const teamNumber = document.getElementsByName('team')[0].value;
    const qualNumber = document.getElementsByName('qual_number')[0].value;
    const scouterName = document.querySelector('input[name="scouter_name"]').value;
    data.comments = encodeURIComponent(data.comments);

    if (!validTeams.includes(parseInt(teamNumber))) {
        alert('The team number is not valid.');
        return false;
    }

    if (qualNumber > 70) {
        alert('The Qual number is not valid.');
        return false;
    }

    const nameValidationRegex = /^[A-Za-z ]+$/;
    if (!nameValidationRegex.test(scouterName)) {
        alert("Please enter a valid name in English.");
        return false;
    }

    // Disable the submit button to prevent multiple submissions
    const submitButton = document.querySelector('input[type="submit"]');
    submitButton.disabled = true;
    submitButton.value = 'Submitting...';

    // Fetch API to send the form data
    fetch('/Scout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Assuming the server responds with JSON
    })
    .then(data => {
        alert('Thanks For Submitting - Excalibur Scouting System Dev Team');
        window.location.reload(true); // Reload the page to reset form and re-enable submit button
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Thanks For Submitting - Excalibur Scouting System Dev Team');
        // Re-enable the submit button if there's an error, allowing the user to try again
        submitButton.disabled = false;
        submitButton.value = 'Submit';
        window.location.reload(true); // Reload the page to reset form and re-enable submit button

    });
}
</script>

<br>
    <input type="submit" value="Submit">
</form>
<br>

{% endblock %}
