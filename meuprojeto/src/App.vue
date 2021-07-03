<template>

  <div class="">

    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Início</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Professor</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#">Aluno</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#">Sobre</a>
          
        </li>

      </ul>
    </div>
  </div>
</nav>

  <br><br><br><br><br><br>

    <div class="container mt-4">

    
	<table class="table table-hover">
  <thead>
    <tr>
      <th>Nº</th>
      <th>Nome</th>
      <th>Nota I Unidade</th>
      <th>Nota II Unidade</th>
      <th>Média</th>
      <th>Situação</th>

    </tr>
  </thead>
  <tbody>
    <tr v-for="user of users" v-bind:key="user">

    <td class="col-1">{{user.id}}</td>
		<td class="col-4">{{user.nome}}</td>
		<td class="col-2">{{user.nota1}}</td>
		<td class="col-2">{{user.nota2}}</td>
		<td class="col-2">{{user.media}}</td>
    <td class="col-2">{{user.situacao}}</td>
    
    </tr>

  </tbody>
</table>
</div>
</div>

  
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return {
      users: []

    }
  },
  created: function(){

   /* 
    axios.post('http://localhost:8000/registration/', {'username': 'paulo', 'password1': 'ifpe2021', 'password2': 'ifpe2021'})
    .then(result => console.log(result))
    .error(error => console.log(error));
  */

  
    axios.get('http://localhost:8000/api/users')
      .then(result => {
        this.users = result.data;
      }).catch(error => {
        console.log(error);
      })
  
}

}
</script>

<style>

  td, th{
    text-align: center;
  }


</style>
