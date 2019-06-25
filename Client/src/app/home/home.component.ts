import { Component, OnInit } from '@angular/core';
import {homeService} from './home.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private homeSrv: homeService, private router: Router) { }

  ngOnInit() {
    this.LoadList();
  }

  
  LoadList(){
    console.log("Before");
    this.homeSrv.GetShoppingLists().subscribe(res => {
      console.log(res);
    })
  }
}
