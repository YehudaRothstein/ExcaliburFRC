function changeValue(elementId, amount) {
    const currentValue = parseInt(document.getElementById(elementId).innerText);
    const newValue = currentValue + amount;

    document.getElementById(elementId).innerText = newValue;

            document.m("hidden_" + elementId).value = newValue;

        }

