from django.db import models

# Create your models here.

class Settings(models.Model):
    _key = models.CharField(max_length=255)
    value1 = models.CharField(max_length=255)
    value2 = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

	# $sql = "INSERT INTO " . $wp_ds_bt_table . " (`_key`, `value1`, `value2`) VALUES ";
	# $sql .= "('symbols_last_updated', '02-02-22', ''),";
	# $sql .= "('api_owner', 'maedotesuba', ''),";
	# $sql .= "('api_secret', 'tSicM8dB1', ''),";
	# $sql .= "('api_key', '0red2ruc3xogw', ''),";
	# $sql .= "('recvWindow', '50000', '')";
	# // $sql .= "('', '', ''),";

class Symbols(models.Model):
    symbol = models.CharField(max_length=20)

    precisionPrice = models.DecimalField(..., max_digits=16, decimal_places=8)
    min_lot_size = models.DecimalField(..., max_digits=16, decimal_places=8)
    isSpotTradingAllowed = models.BooleanField(default=True)
    isMarginTradingAllowed = models.BooleanField(default=True)
    permissions = models.CharField(max_length=50)
    lastPrice = models.DecimalField(..., max_digits=16, decimal_places=8)
    asset_volume = models.DecimalField(..., max_digits=16, decimal_places=8)
    busd_volume = models.DecimalField(..., max_digits=16, decimal_places=8)
    priceChange = models.DecimalField(..., max_digits=16, decimal_places=8)
    priceChangePercent = models.DecimalField(..., max_digits=16, decimal_places=8)
    currentAsset = models.DecimalField(..., max_digits=16, decimal_places=8)
    busdValue = models.DecimalField(..., max_digits=16, decimal_places=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
