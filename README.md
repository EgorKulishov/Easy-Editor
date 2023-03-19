# Easy-Editor
<h3><center>JavaScript Click Counter</center></h3>
<div>
    <center><h3 id="counter-label">0</h3></center>
</div>
<center>
    <div>
        <button onclick="incrementClick()">Click Me</button>
        <button onclick="resetCounter()">Reset</button>
    </div>
</center>
<script>
 var counterVal = 0;

function incrementClick() {
    updateDisplay(++counterVal);
}

function resetCounter() {
    counterVal = 0;
    updateDisplay(counterVal);
}

function updateDisplay(val) {
    document.getElementById("counter-label").innerHTML = val;
}
</script>
