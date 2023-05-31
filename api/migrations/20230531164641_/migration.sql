-- CreateTable
CREATE TABLE "Items" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "created_at" TIMESTAMPTZ(6) DEFAULT CURRENT_TIMESTAMP,
    "name" TEXT NOT NULL,
    "price" BIGINT NOT NULL,

    CONSTRAINT "Items_pkey" PRIMARY KEY ("id")
);
