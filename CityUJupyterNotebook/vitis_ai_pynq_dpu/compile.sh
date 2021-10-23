ARCH=./arch.json
OUTDIR=./xmodel_Ultra96
NET_NAME=quantized_model
MODEL=./quantized_model.h5

compile() {
	vai_c_tensorflow2 \
		--model		$MODEL \
		--arch		$ARCH \
		--output_dir	$OUTDIR \
		--net_name	$NET_NAME
	}

compile 2>&1 | tee compile.log