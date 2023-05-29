console.log("Ola mundo")

const socket = new WebSocket('ws://' + window.location.host + '/ws/dashboard_aluguel/')

socket.onmessage = function(e){
    console.log('Server ' + e.data);
};

socket.onopen = function(e){
    socket.send(JSON.stringify({
        'message':'Hello from Client',
        'sender': 'teste sender'
    }));
};