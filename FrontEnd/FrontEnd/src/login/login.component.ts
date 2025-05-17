import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'login',
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
 constructor(private router: Router) {}

 goHome(){
  this.router.navigate(['/home']);
 }
}
