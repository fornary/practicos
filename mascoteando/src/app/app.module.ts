import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatToolbarModule} from '@angular/material/toolbar';

import {MatIconModule} from '@angular/material/icon';
import { FooterComponent } from './componetes/footer/footer.component';
import { BodyComponent } from './componetes/body/body.component';
import { NavbarComponent } from './componetes/navbar/navbar.component';
import { HeaderComponent } from './componetes/header/header.component';


@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    BodyComponent,
    NavbarComponent,
    HeaderComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
