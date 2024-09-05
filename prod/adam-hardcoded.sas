options dlcreatedir;
libname outputs "/workflow/outputs"; /* All outputs must go to this directory at workflow/inputs/<NAME OF OUTPUT>y */ 
libname datasetA "/mnt/data/snapshots/DatasetA/1";
libname datasetB "/mnt/data/snapshots/DatasetB/1";
libname datasetC "/mnt/data/snapshots/DatasetC/1";

/* Write the final ADAM output */
data outputs.adam;
    merge datasetA.sv datasetB.ts datasetC.ta;
run;


