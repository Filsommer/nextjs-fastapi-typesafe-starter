/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Get Hello
     * @returns string Successful Response
     * @throws ApiError
     */
    public static getHello(): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/python',
        });
    }

}
