import { Routes } from '@angular/router';
import { LoginComponent } from '../login/login.component';
import { AppComponent } from './app.component';
import { ProductosComponent } from '../productos/productos.component';
import { AlmacenComponent } from '../almacen/almacen.component';
import { HomeComponent } from '../home/home.component';

export const routes: Routes = [
  { path: '', component: LoginComponent},
  { path: 'home', component: HomeComponent },
  { path: 'productos', component: ProductosComponent },
  { path: 'almacen', component: AlmacenComponent },
];
