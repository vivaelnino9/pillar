import { Injectable } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient} from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class OrganizationService {
  API_URL  =  'http://localhost:8000/organizations/';

  constructor(private httpClient: HttpClient) {}

  getOrganizations(){
      return this.httpClient.get(this.API_URL);
  }

  makeOrganization(organizationForm: FormGroup){
    return this.httpClient.post<any>(this.API_URL, organizationForm.value)
  }
}
