/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Items } from "../models/Items";
import type { ResponseMessage } from "../models/ResponseMessage";

import type { CancelablePromise } from "../core/CancelablePromise";
import { OpenAPI } from "../core/OpenAPI";
import { request as __request } from "../core/request";

export class ItemsService {
  /**
   * Get Items
   * @returns Items Successful Response
   * @throws ApiError
   */
  public static getItems(): CancelablePromise<Array<Items>> {
    return __request(OpenAPI, {
      method: "GET",
      url: "/api/items",
    });
  }

  /**
   * Create Item
   * @param requestBody
   * @returns ResponseMessage Successful Response
   * @throws ApiError
   */
  public static createItem(requestBody: Items): CancelablePromise<ResponseMessage> {
    return __request(OpenAPI, {
      method: "POST",
      url: "/api/items",
      body: requestBody,
      mediaType: "application/json",
      errors: {
        422: `Validation Error`,
      },
    });
  }
}
