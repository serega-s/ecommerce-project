<template>
  <div class="container">
    <div>
      <h1>Order:</h1>
      <div class="row">
        <div class="col-md-8">
          <div class="list-group list-group-flush">
            <div class="list-group-item">
              <h2>Shipping</h2>
              <p><strong>Name: </strong> sergei</p>
              <p>
                <strong>Email: </strong
                ><a href="mailto:sergei@sergei.com">sergei@sergei.com</a>
              </p>
              <p><strong>Shipping: </strong>12d, 2d 3563553112e, Россия</p>
              <div role="alert" class="fade alert alert-warning show">
                Not Delivered
              </div>
            </div>
            <div class="list-group-item">
              <h2>Payment Method</h2>
              <p><strong>Method: </strong>PayPal</p>
              <div role="alert" class="fade alert alert-warning show">
                Not Paid
              </div>
            </div>
            <div class="list-group-item">
              <h2>Order Items</h2>
              <div class="list-group list-group-flush">
                <div class="list-group-item">
                  <div class="row">
                    <div class="col-md-1">
                      <img
                        src="/images/mouse_E2IrCGI.jpg"
                        alt="Logitech G-Series Gaming Mouse"
                        class="img-fluid rounded"
                      />
                    </div>
                    <div class="col">
                      <a href="#/product/5">Logitech G-Series Gaming Mouse</a>
                    </div>
                    <div class="col-md-4">1 X $49.99 = $49.99</div>
                  </div>
                </div>
                <div class="list-group-item">
                  <div class="row">
                    <div class="col-md-1">
                      <img
                        src="/images/camera_LfFS0wx.jpg"
                        alt="Cannon EOS 80D DSLR Camera"
                        class="img-fluid rounded"
                      />
                    </div>
                    <div class="col">
                      <a href="#/product/4">Cannon EOS 80D DSLR Camera</a>
                    </div>
                    <div class="col-md-4">1 X $929.29 = $929.29</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <div class="list-group list-group-flush">
              <div class="list-group-item uppercase"><h2>Order Summary</h2></div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Items:</div>
                  <div class="col">$979.28</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Shipping:</div>
                  <div class="col">$0.00</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Tax:</div>
                  <div class="col">$80.30</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Total:</div>
                  <div class="col">$1059.58</div>
                </div>
              </div>
              <div class="list-group-item">
                <div
                  role="status"
                  class="spinner-border"
                  style="height: 100px; width: 100px; margin: auto; display: block;"
                >
                  <span class="sr-only">Loading...</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Order",
  data() {
    return {}
  },
}
</script>

<style></style>
