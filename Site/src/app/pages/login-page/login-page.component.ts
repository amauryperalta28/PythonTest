import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {AuthService} from "../../services/auth.service";

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent{
  username = '';
  password = '';
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  onLogin() {
    this.authService.login(this.username, this.password).subscribe(
      (success) => {
        if (success) {
          this.router.navigate(['/home']); // Redirigir a Home
        } else {
          this.errorMessage = 'Login failed';
        }
      },
      (error) => {
        this.errorMessage = 'Invalid credentials';
      }
    );
  }

}
