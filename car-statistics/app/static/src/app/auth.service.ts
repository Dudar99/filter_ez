import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {User} from "./models/user";
import {Observable} from "rxjs";
import {tap} from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  login_api_url = "api/login";
  register_api_url = "api/register";
  confirm_url = "api/confirm/";
  logout_api_url = "api/logout";

  constructor(
      private _http: HttpClient,
      ) { }

  toRegister(user: User) : Observable<any> {
    return this._http.post<any>(this.register_api_url, user)
        .pipe(
          tap(
              data => console.log(data),
              error => console.log(error)
          )
        );
  }

  toLogin(user: User) : Observable<any> {
    return this._http.post<any>(this.login_api_url, user);
  }

  toLogout(user: User) : Observable<any> {
    return this._http.post<any>(this.logout_api_url, user);
  }
  confirmEmail(token: string) : Observable<any> {

    return this._http.get<any>(this.confirm_url+token);
  }

}
