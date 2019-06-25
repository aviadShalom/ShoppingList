import {Inject} from '@angular/core';
import {DOCUMENT} from '@angular/common';


export abstract class LoaderService {
  constructor(@Inject(DOCUMENT) protected document: any) {
  }

  protected showLoader(): void {
    const el = this.getEl('black-lightbox');
    if (el) {
      el.classList.add('show');
    }
  }

  protected hideLoader(): void {
    const el = this.getEl('black-lightbox');
    if (el) {
      el.classList.remove('show');
    }
  }

  private getEl(_el: string): HTMLElement | null {
    const el = this.document.getElementById(_el);
    if (!el) {
      return null;
    }
    return el;
  }
}
