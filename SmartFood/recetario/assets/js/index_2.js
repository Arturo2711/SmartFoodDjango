var goal = 0; // La meta ahora se establecerá a través del input
var consumed = 0;

function consumeCalories() {
    var goalInput = document.getElementById("goal-input");
    goal = parseInt(goalInput.value) || 0;

    var consumeInput = document.getElementById("consume-input");
    var consumeAmount = parseInt(consumeInput.value) || 0;

    consumed += consumeAmount;
    updateGoalDisplay();
    updateProgress();
    updateResult();
    consumeInput.value = ""; // Limpiar el campo de entrada
}

function registerFood() {
    var food = prompt("Ingresa el nombre del alimento:");
    if (food) {
        alert("Has registrado el alimento: " + food);
    }
}

function updateGoalDisplay() {
    var goalDisplay = document.getElementById("goal-display");
    goalDisplay.textContent = "Meta de calorías: " + goal;
}

function updateProgress() {
    var progress = (consumed / goal) * 100;
    if (progress > 100) {
        progress = 100;
    }

    var progressBar = document.getElementById("progress-bar");
    progressBar.style.width = progress + "%";
    progressBar.textContent = progress.toFixed(2) + "%";
}

function updateResult() {
    var result = document.getElementById("result");
    var today = new Date().toLocaleDateString();
    result.textContent = `Consumido el ${today}: ${consumed} calorías`;
}

function showMealPlan() {
    alert("Aquí se mostrará el plan alimentario.");
}