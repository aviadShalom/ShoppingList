import { Component, OnInit,TemplateRef } from '@angular/core';
import {homeService} from './home.service';
import { Router } from '@angular/router';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  shoppingList:any;
  modalRef: BsModalRef;
  newListName:string;
  deleted_item:any;

  constructor(private homeSrv: homeService, private router: Router, private modalService: BsModalService) { }

  ngOnInit() {
    this.LoadList();
  }

  
  LoadList(){    
    this.homeSrv.GetShoppingLists().subscribe(res => {
      console.log(res);
      this.shoppingList = res.Data;
    })
  }
  itemSelected(itemID:any){    
    let queryParams = "?itemID="+itemID
    this.router.navigateByUrl("ShoppingList" + queryParams);
  }

  openModal(template: TemplateRef<any>) {
    console.log(template.elementRef);
    this.modalRef = this.modalService.show(template,Object.assign({}, { class: 'gray modal-md' }));
  }

  CreateList(){
    console.log(this.newListName);
    this.homeSrv.CreateNewShoppingList(this.newListName).subscribe( res => {
      console.log(res)
      this.LoadList();
    })
  }

  DeleteItemConfirm(itemID,template){    
    this.deleted_item = itemID
    this.modalRef = this.modalService.show(template,Object.assign({}, { class: 'gray modal-md' }));    
  }

  DeleteItemAnswer(answer){
    if(answer == 1){
      this.homeSrv.DeleteShoppingList(this.deleted_item).subscribe( res => {
        if (res == "1"){
          this.LoadList();
        }
      })
      this.modalRef.hide();
    }
    else if(answer == 0){
      console.log("cancel");
      this.modalRef.hide();
    }

  }
}
