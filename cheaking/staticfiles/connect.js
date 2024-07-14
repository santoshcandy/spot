console.log("db to ui")
/*
document.addEventListener('DOMContentLoaded', function () {
    fetch('/reg/')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const contactsList = document.getElementById('details-list');
            data.forEach(contact => {
                const li = document.createElement('li');
                li.textContent = `${contact.Name}: ${contact.PhoneNumber} - ${contact.Location}`;
                contactsList.appendChild(li);
            });
        })  
});
*/


document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/contacts/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(data)
            const contactsList = document.getElementById('contacts-list');
            data.forEach(contact => {
                const li = document.createElement('tr');
                li.innerHTML = `
                <td>${contact.Name}</td>

                <td>${contact.Phone} </td>

                <td>${contact.Location}</td>
                
                <td>${contact.Service}</td>

                
                
                
                
                 `;
                contactsList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching contacts:', error);
            // Log the response text for debugging
            fetch('/api/contacts/')
                .then(response => response.text())
                .then(text => console.log('Response text:', text));
        });
});
