import { Routes } from '@angular/router';
import { LoginComponent } from '../login/login.component';
import { AppComponent } from './app.component';
import { ProductosComponent } from '../productos/productos.component';
import { AlmacenComponent } from '../almacen/almacen.component';
import { HomeComponent } from '../home/home.component';

export const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'login', component: LoginComponent },
  { path: 'productos', component: ProductosComponent },
  { path: 'almacen', component: AlmacenComponent },
];
