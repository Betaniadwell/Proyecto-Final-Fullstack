let usuariosRegistrados = [{userEmail: 'admin@admin.com',userPassword: 'admin'}];

document.getElementById('formLogin').addEventListener('submit', function(e) {
    e.preventDefault();})

function loguear()

{
let userEmail=document.getElementById('userEmail').value;
let userPassword=document.getElementById('userPassword').value;

    


if (userEmail== 'admin@admin.com' && userPassword == 'admin') {
    window.location.href ='http://127.0.0.1:5000';}
    
else {
    alert('Usuario o contraseña incorrecta. Por favor intentalo de nuevo');
    }

    
}
