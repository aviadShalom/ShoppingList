import {Injectable} from '@angular/core';
import {HttpService} from '../core/http.service';
import {Router} from '@angular/router';

@Injectable({
    providedIn:'root'
})

export class homeService {
    constructor(private httpSrv: HttpService, private router:Router){}

    GetShoppingLists(){
        return this.httpSrv.post('GetShoppingList');
    }
}