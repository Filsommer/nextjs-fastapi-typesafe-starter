/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

/**
 * Used when creating a new Item record, as there's no need to specify an id (db will autogenerate one)
 */
export type ItemCreator = {
    id?: string;
    created_at?: string;
    name: string;
    price: number;
};

