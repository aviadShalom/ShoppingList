import { Component, OnInit } from '@angular/core';
import {homeService} from './home.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  shoppingList:any;

  constructor(private homeSrv: homeService, private router: Router) { }

  ngOnInit() {
    this.LoadList();
  }

  
  LoadList(){
    console.log("Before");
    this.homeSrv.GetShoppingLists().subscribe(res => {
      this.shoppingList = res;
    })
  }
  itemSelected(itemID:any){
    console.log(itemID);
    let queryParams = "?itemID="+itemID
    this.router.navigateByUrl("ShoppingList" + queryParams);
  }
}
