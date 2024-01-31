  function updateCounter(change, counterId, category) {
        let counterValue = parseInt(document.getElementById(counterId).value);
        counterValue = Math.max(0, counterValue + change);
        document.getElementById(counterId).value = counterValue;

        let totalCounterId = 'totalCounter' + category;
        let totalCounterValue = parseInt(document.getElementById(totalCounterId).value);
        totalCounterValue = Math.max(0, totalCounterValue + change);
        document.getElementById(totalCounterId).value = totalCounterValue;
    }

           function changeValue(elementId, amount) {
            var currentValue = parseInt(document.getElementById(elementId).innerText);
            var newValue = currentValue + amount;

            document.getElementById(elementId).innerText = newValue;

            document.m("hidden_" + elementId).value = newValue;
        }

        function updateCounter(change, counterId, category) {

}