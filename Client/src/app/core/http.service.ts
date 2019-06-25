import {Inject, Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {throwError} from 'rxjs';
import {catchError, finalize, map} from 'rxjs/operators';
import {LoaderService} from './loader.service';
import {DOCUMENT} from '@angular/common';
import { environment } from '../../environments/environment';
@Injectable({
  providedIn: 'root'
})
export class HttpService extends LoaderService {

  private mainUrl: string;


  constructor(private httpClient: HttpClient, @Inject(DOCUMENT) protected document: any) {
    super(document);
    this.mainUrl = environment.apiEndpoint;
  }

  get(url: string, param = {}, showLoader = true) {
    if (showLoader) {
      this.showLoader();
    }
    return this.httpClient.get(`${this.mainUrl}${url}`, {params: param}).pipe(
      map((res) => {
        console.log(res);
        return res;
      }),
      catchError(this.handleError.bind(this)),
      finalize(() => !!showLoader ? this.hideLoader() : null)
    );
  }

  post(url: string, data = {}, headers = {}, showLoader = false) {
    if (showLoader) {
      this.showLoader();
    }
    return this.httpClient.post(`${this.mainUrl}${url}`, data, headers)
      .pipe(map(this.transformResponse),
        catchError(this.handleError.bind(this)),
        finalize(() => !!showLoader ? this.hideLoader() : null)
      );
  }

  private transformResponse(response: any) {
    if (!response.PayLoad) {
      return response;
    }
    if (response.IsError) {
      throw new Error(`Bad response: ${response}`);
    }
    return response.PayLoad;
  }

  private handleError(error: HttpErrorResponse) {

    console.log(error.message);
    return throwError(`Something bad happened: please try again later`);
  }
}
